#!/usr/bin/env python3
"""Convert SKILL.md files with descriptions <=200 chars (Claude Skills v1 spec)."""

import shutil
from pathlib import Path

SKILL_METADATA = {
    "mood-curator": {
        "description": "Curate visual mood for AI video. Generates 5-color palette, texture, light character, mood keywords. Use when starting a video project or realigning visual tone. Part of kkirikkiri team.",
        "category": "agents/kkirikkiri"
    },
    "reference-scout": {
        "description": "Convert director/film/brand names to safe technical vocabulary for AI video. MPA copyright safe. Use when scouting visual references or avoiding style imitation risk. kkirikkiri team.",
        "category": "agents/kkirikkiri"
    },
    "aesthetic-director": {
        "description": "Integrate mood and references into look_spec for video. Critical interface between kkirikkiri and pumasi teams. Use to consolidate colors, lens, lighting, grade, movement into one spec.",
        "category": "agents/kkirikkiri"
    },
    "narrative-weaver": {
        "description": "Design emotional arc and narrative beats for AI video. 5 elements per beat (emotion, meaning, anchor, audio, time). Use when emotional flow is critical or planning series DNA. kkirikkiri team.",
        "category": "agents/kkirikkiri"
    },
    "script-writer": {
        "description": "Write video scripts from narrative arcs. Translates beats into scenes with subtitles, CTA, AI disclosure. Real-time guardrail check. Use when converting narrative into scenes. pumasi team.",
        "category": "agents/pumasi"
    },
    "shot-designer": {
        "description": "Design shot-by-shot breakdown for video. Generates shotlist.csv with 5-layer cinematic spec (size, angle, lens, lighting, look) plus clip_id columns. Use when decomposing scenes. pumasi team.",
        "category": "agents/pumasi"
    },
    "prompt-engineer": {
        "description": "Generate AI image and video prompts via 4-stage pipeline (foundations to cinematic to adapter to seedance). Use when converting shot designs into prompts for Nano Banana, GPT, Seedance, Kling.",
        "category": "agents/pumasi"
    },
    "motion-director": {
        "description": "Direct facial expression and body motion using FACS Action Units with intensity (A-E) plus natural language. Use only for shots showing faces. pumasi team.",
        "category": "agents/pumasi"
    },
    "editor": {
        "description": "Specify post-production for AI video. Generates edit_decision_list with trims, transitions, audio, color grade, exports. Auto-calls music-rights-check. Use after clip generation. pumasi team.",
        "category": "agents/pumasi"
    },
    "intake-router": {
        "description": "Route user video requests to right team and skills. Classifies format, purpose, platform, duration, AI rights, clip strategy. Use at entry point of every video task to determine workflow.",
        "category": "shared"
    },
    "cinematic-shot": {
        "description": "Specify cinematic shots in 5 layers: size, angle, lens, lighting, look. Use when designing shots or as Step 2 of prompt-engineer pipeline. Unified vocabulary for visual specs.",
        "category": "shared"
    },
    "facs-expression": {
        "description": "Specify facial expressions using FACS Action Units AU1-AU45 with intensity A-E (ads use A-C), M Code, Gross Behavior. Use when faces need precise expression spec for AI video generation.",
        "category": "shared"
    },
    "seedance-prompt": {
        "description": "Generate Seedance 2.0 multimodal prompts with 4-15s HARD LIMIT awareness. 12-file input, source binding (@image1), time markers. Use as Step 4 of prompt-engineer pipeline for video generation.",
        "category": "shared"
    },
    "mv-builder": {
        "description": "Build music videos via 7-step methodology: analysis, concept, lyric mapping, motifs, shotlist, generation, editing. Clip-based mapping for videos over 15 seconds. Use for music video work.",
        "category": "shared"
    },
    "character-pool": {
        "description": "Manage character sheets for video series: demographics, face, wardrobe, demeanor, facs_defaults, what_to_avoid, ai_rights_notes. Use at series start; lock after V1 for consistency.",
        "category": "shared"
    },
    "series-variation": {
        "description": "Manage variation matrix for video series. Tracks LOCKED assets (brand, color, look, narrative) vs VARIABLE dimensions (persona, location, protagonist, motif). Use for multi-episode campaigns.",
        "category": "shared"
    },
    "post-production-spec": {
        "description": "Standard JSON spec for video post-production: transitions, text overlays, audio tracks, color grade, edit_decision_list, export variants. Use as deliverable format from editor agent.",
        "category": "shared"
    },
    "guardrail-check": {
        "description": "4-Part guardrail for AI video: Korean ad law, AI rights (OpenAI/SAG-AFTRA/MPA/Vimeo), visual (real-person/logos), AI checklist. Use before distribution. Auto-triggers on AI generation.",
        "category": "shared"
    },
    "visual-bible": {
        "description": "Master visual bible for video series. 7 sections: brand, color, typography, look_spec, characters, motifs, taboos. Init/lock/validate/export ops. Use to lock V1 for V2-Vn consistency.",
        "category": "shared"
    },
    "image-prompt-foundations": {
        "description": "Foundational image prompting: removes 3 ambiguity types (abstract emotion, subjective qualifiers, broad subjects), requires shadow spec, uses 5-layer structure. Use as Step 1 of prompt pipeline.",
        "category": "shared"
    },
    "model-adapter": {
        "description": "Adapt prompts for AI models: GPT Image 2, Nano Banana Pro, Seedance 2.0/1.5 Pro, Kling 3.0. Auto-blocks director/film names for MPA safety. Use as Step 3 of prompt-engineer pipeline.",
        "category": "shared"
    },
    "qa-review": {
        "description": "6-dimension QA for AI video: character consistency, artifacts, lipsync, cut rhythm, prompt drift, evidence. Plus AI rights checks. 3-cycle limit. Use after generation, before confirmation.",
        "category": "shared"
    },
    "production-brief": {
        "description": "Package video deliverables in 5 standard files (brief, characters, shotlist, image/video prompts) plus clip_segmentation.json and clips/ directory. Use at project end for client handoff.",
        "category": "shared"
    },
    "series-closer": {
        "description": "Design final episode of video series via 3 closure types: Reprise Montage (5+ eps), Synthesis Landscape (3-4 eps), Compressed Narrative (8+ or standalone). Hybrids possible. Use for finale.",
        "category": "shared"
    },
    "copy-tone-check": {
        "description": "Check copy tone across video series via 5 dimensions: tone bounds, addressing, sentence endings, metaphor categories, length rhythm. Use after writing episode copies for consistency check.",
        "category": "shared"
    },
    "music-rights-check": {
        "description": "Check music rights across 5 categories: Self-Composed, Royalty-Free, Sync, AI Generated (SUNO), Voice Cloning (SAG-AFTRA). Auto-called after editor. Use to verify license before delivery.",
        "category": "shared"
    },
    "workflow-curator": {
        "description": "Meta-skill diagnosing OpenCrab workflows. Inventories packs, classifies relevance, detects duplicates via Jaccard, proposes streamlined workflow. Diagnosis only, never modifies automatically.",
        "category": "shared"
    },
    "clip-segmentation": {
        "description": "Segment videos over 15s into clips for Seedance 2.0 HARD LIMIT. 4 patterns: Beat-Boundary, Action-Boundary, Match-Cut, Detail Sequence. Sweet spot 8-12s per clip. v0.6 critical for long video.",
        "category": "shared"
    },
}


def convert_skill_file(source_path, target_dir, skill_name, metadata):
    content = source_path.read_text(encoding="utf-8")
    description = metadata["description"]
    assert len(description) <= 200, f"{skill_name}: {len(description)} chars"
    
    frontmatter = f"---\nname: {skill_name}\ndescription: {description}\n---\n\n"
    
    skill_folder = target_dir / metadata["category"] / skill_name
    skill_folder.mkdir(parents=True, exist_ok=True)
    
    skill_md = skill_folder / "SKILL.md"
    skill_md.write_text(frontmatter + content, encoding="utf-8")
    return skill_md


def main():
    source_root = Path("/home/claude/video-production-system/skills")
    target_root = Path("/home/claude/vps-skills-github/skills")
    
    print("Pre-check description lengths:")
    all_ok = True
    for name, meta in SKILL_METADATA.items():
        n = len(meta["description"])
        flag = "✓" if n <= 200 else "✗"
        print(f"  {flag} {name}: {n}")
        if n > 200:
            all_ok = False
    
    if not all_ok:
        print("FAIL: some descriptions exceed 200 chars")
        return
    
    print("\nAll under 200. Cleaning target...")
    if target_root.exists():
        shutil.rmtree(target_root)
    
    skill_files = {
        "agents/kkirikkiri/mood-curator-SKILL.md": "mood-curator",
        "agents/kkirikkiri/reference-scout-SKILL.md": "reference-scout",
        "agents/kkirikkiri/aesthetic-director-SKILL.md": "aesthetic-director",
        "agents/kkirikkiri/narrative-weaver-SKILL.md": "narrative-weaver",
        "agents/pumasi/script-writer-SKILL.md": "script-writer",
        "agents/pumasi/shot-designer-SKILL.md": "shot-designer",
        "agents/pumasi/prompt-engineer-SKILL.md": "prompt-engineer",
        "agents/pumasi/motion-director-SKILL.md": "motion-director",
        "agents/pumasi/editor-SKILL.md": "editor",
        "intake-router-SKILL.md": "intake-router",
        "cinematic-shot-SKILL.md": "cinematic-shot",
        "facs-expression-SKILL.md": "facs-expression",
        "seedance-prompt-SKILL.md": "seedance-prompt",
        "mv-builder-SKILL.md": "mv-builder",
        "character-pool-SKILL.md": "character-pool",
        "series-variation-SKILL.md": "series-variation",
        "post-production-spec-SKILL.md": "post-production-spec",
        "guardrail-check-SKILL.md": "guardrail-check",
        "visual-bible-SKILL.md": "visual-bible",
        "image-prompt-foundations-SKILL.md": "image-prompt-foundations",
        "model-adapter-SKILL.md": "model-adapter",
        "qa-review-SKILL.md": "qa-review",
        "production-brief-SKILL.md": "production-brief",
        "series-closer-SKILL.md": "series-closer",
        "copy-tone-check-SKILL.md": "copy-tone-check",
        "music-rights-check-SKILL.md": "music-rights-check",
        "workflow-curator-SKILL.md": "workflow-curator",
        "clip-segmentation-SKILL.md": "clip-segmentation",
    }
    
    count = 0
    for rel_path, skill_name in skill_files.items():
        source = source_root / rel_path
        if source.exists() and skill_name in SKILL_METADATA:
            convert_skill_file(source, target_root, skill_name, SKILL_METADATA[skill_name])
            count += 1
            print(f"  ✓ {skill_name}")
    
    print(f"\n{count} skills converted")


if __name__ == "__main__":
    main()
