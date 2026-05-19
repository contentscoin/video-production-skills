---
name: workflow-curator
description: Meta-skill diagnosing OpenCrab workflows. Inventories packs, classifies relevance, detects duplicates via Jaccard, proposes streamlined workflow. Diagnosis only, never modifies automatically.
---

# Workflow Curator

오픈크랩 **영상제작 워크플로우의 구조를 진단하고 재구성**하는 메타 스킬.
현재 워크플로우의 비효율을 분석하고 최적화된 워크플로우를 제안합니다.

## When to use

- 오픈크랩 워크플로우에 영상 무관 팩이 섞여 있을 때
- 같은 정보를 여러 팩이 중복 제공할 때
- 새 팩 추가 시 기존 워크플로우와의 관계 점검
- 컨텍스트 로딩이 너무 무거워졌을 때

## 현재 워크플로우 진단 (2026-05-18 시점)

오픈크랩 워크플로우 ID: `a00d4e46-6f1c-40e6-bbec-3198e32d82f0`
이름: "영상제작"

```
Step 1: korea_card_graph_v4 (영상 무관)        ❌
Step 2: pritzker_2000_present_persona (영상 무관) ❌
Step 3: movie_seedance_pack (87 docs, 1000 nodes) ⭐ 메인
Step 4: AI 단편영화 가이드                      ⚠️ Step 3에 통합됨
Step 5: FACS 표정 가이드                        ⚠️ Step 3에 통합됨
Step 6: 시네마틱 이미지 가이드                  ⚠️ Step 3에 통합됨
Step 7: 뮤직비디오 가이드                       ⚠️ Step 3에 통합됨
Step 8: Seedance 2.0 프롬프팅 가이드            ⚠️ Step 3에 통합됨
```

**문제**:
- 영상 무관 팩 2개로 컨텍스트 윈도우 낭비
- Step 4-8은 Step 3에 모두 포함되어 있어 중복

**해결 후 이상적 구조**:
```
Step 1: movie_seedance_pack (단독, 메인 컨텍스트)
```

또는 (보강이 필요한 경우):
```
Step 1: movie_seedance_pack (메인)
Step 2: (보강 팩 — 신규 모델 가이드, 신규 정책 자료 등)
```

## 워크플로우 진단 알고리즘

### Step A: 워크플로우 인벤토리

```python
1. opencrab_list_workflows(query="영상")
2. 각 워크플로우의 steps 추출
3. 각 step의 package_id로 팩 메타데이터 조회 (opencrab_search_packs)
```

### Step B: 팩별 카테고리 분류

```python
for each step:
  - 팩 제목·설명 분석
  - 카테고리 자동 분류:
    * "core_video_pack" (영상 제작 메인)
    * "supplementary_video" (영상 제작 보강)
    * "tangentially_related" (영상 관련 일반)
    * "unrelated" (영상 무관)
```

분류 키워드:
- core_video_pack: "seedance", "video", "영상", "filmmaking"
- supplementary_video: "image generation", "music video", "FACS", "cinematic"
- tangentially_related: "ai", "creative", "branding"
- unrelated: 그 외 모든 키워드 (carbon_graph, persona, card 등)

### Step C: 중복 검출

```python
for each pair of packs:
  - 키워드 overlap 분석 (자카드 유사도)
  - 0.7 이상이면 중복 의심
  - 0.9 이상이면 중복 확정
```

### Step D: 재구성 제안

```yaml
recommended_workflow:
  name: "영상제작 (정리됨)"
  rationale: "movie_seedance_pack이 4-8 단계를 모두 포함"
  
  steps_to_remove:
    - reason: "영상 무관"
      packs: ["korea_card_graph_v4", "pritzker_persona"]
    - reason: "movie_seedance_pack에 통합됨"
      packs: ["ai_short_film", "facs_guide", "cinematic_image", "music_video", "seedance_2_prompt"]
  
  steps_to_keep:
    - "movie_seedance_pack"
  
  steps_to_consider_adding:
    - "Anthropic Claude AI 가이드라인 팩 (있다면)"
    - "한국 광고법 팩 (자체 구성)"
    - "다국어 카피 팩 (필요 시)"

  final_proposed_steps:
    - step: 1
      package: "movie_seedance_pack"
      instruction: "Use movie_seedance_pack as the primary video production context."
```

## 워크플로우 재구성 명령 (사용자가 실행)

⚠️ **이 스킬은 자동으로 워크플로우를 수정하지 않습니다**. 진단 + 제안만.
실제 수정은 오픈크랩 UI에서 사용자가 직접.

추천 작업 순서:
```
1. 진단 리포트 검토
2. 오픈크랩 UI에서 "영상제작" 워크플로우 편집
3. Step 1, 2 (korea_card_graph, pritzker) 삭제
4. Step 4-8 (가이드 5종) 삭제 — movie_seedance_pack에 포함됨
5. 저장 → 새 컨텍스트로 재로드
```

## Output Format

```yaml
workflow_curation_report:
  workflow_id: "a00d4e46-6f1c-40e6-bbec-3198e32d82f0"
  workflow_name: "영상제작"
  analyzed_at: "2026-05-18"
  
  current_state:
    total_steps: 8
    estimated_context_size: "~2,500 nodes total"
    categorization:
      core_video_pack: 1  # movie_seedance_pack
      supplementary_video: 5  # 가이드 5종
      unrelated: 2  # korea_card, pritzker
  
  issues:
    - severity: "high"
      type: "unrelated_packs"
      packs: ["korea_card_graph_v4", "pritzker_persona"]
      impact: "컨텍스트 윈도우의 ~40% 낭비"
    
    - severity: "medium"
      type: "redundant_packs"
      packs: ["ai_short_film", "facs_guide", "cinematic_image", "music_video", "seedance_2_prompt"]
      impact: "movie_seedance_pack에 포함된 자료 중복"
  
  recommendations:
    immediate_actions:
      - "Step 1, 2 삭제 (영상 무관)"
      - "Step 4-8 삭제 (중복)"
    
    proposed_final_structure:
      steps:
        - step: 1
          package_id: "7b76f28b-53c5-4d77-be5b-e2e3cd1e69d3"
          package_title: "movie_seedance_pack"
    
    estimated_improvement:
      context_reduction: "60-65%"
      relevance_increase: "100% (모든 단계가 영상 관련)"
      load_time: "체감 가능한 개선"
  
  pre_action_checklist:
    - "현재 워크플로우 백업"
    - "movie_seedance_pack이 최신 버전인지 확인"
    - "삭제할 팩이 다른 워크플로우에서 쓰이는지 확인"
```

## 핵심 원칙

### 진단만, 자동 수정 안 함
워크플로우는 사용자 자산. 자동 수정 위험. 제안만 하고 실제 수정은 사용자가.

### 백업 항상 권고
수정 전 현재 구조를 메모해두기. 잘못된 수정 시 복구용.

### 다른 워크플로우 영향 확인
같은 팩이 여러 워크플로우에서 쓰일 수 있음. 삭제 전 영향 범위 점검.

## 휴리스틱

- **컨텍스트 윈도우의 60% 이상**이 영상 무관이면 즉시 정리 권고
- **중복도 0.8 이상**인 팩은 통합 권고
- **새 팩 추가 시**는 항상 기존 팩과의 중복 점검
- **워크플로우 step 수는 5개 이하**가 운영 효율적
- **각 step의 instruction은 명확하게** — "use as next context layer"보단 구체적

## 미래 확장: 자동 큐레이션 (v0.6 후보)

향후 가능한 보강:
1. **자동 워크플로우 생성**: 사용자 의도 → 적합한 팩 자동 선택 + 순서 결정
2. **컨텍스트 최적화**: 토큰 윈도우 한도 내에서 가장 가치 높은 팩 조합 자동 추천
3. **팩 간 의존성 그래프**: 어떤 팩이 다른 팩의 전제인지 시각화
4. **사용 빈도 분석**: 자주 쓰는 팩 조합을 새 워크플로우로 자동 제안

## 협업 인터페이스

### intake-router와 협업
- intake-router가 작업 시작 시 → workflow-curator가 현재 워크플로우 적합성 점검
- 부적합 시 권고

### 다른 메타 스킬들과 협업
- production-brief의 "오픈크랩 컨텍스트" 섹션 자동 갱신
- 시리즈 완료 후 사용된 팩 → 워크플로우 효율성 회고

## 시스템 호출

- **상위**: 사용자가 직접 호출 (메타 작업)
- **하위**: 진단 리포트 출력
- **연관**: intake-router (워크플로우 적합성 점검)
- **결과**: workflow_curation_report YAML

## 청사진 매핑

청사진 외 영역. 우리 시스템 고유 메타 스킬.

## 오픈크랩 컨텍스트

- 오픈크랩 자체의 워크플로우·팩·노드 API 활용
- opencrab_list_workflows, opencrab_search_packs, opencrab_list_nodes
