# Examples

Real outputs produced by Video Production System v0.6 in actual production work.

## brand-film-30s/

A complete 30-second cinematic brand film output package. Demonstrates the full v0.6 workflow including:

- Mirror structure (CLIP-1 dawn ↔ CLIP-8 dusk)
- ECU triple via 4s generation + trim (CLIP-2/3/4)
- Hero shot single clip (CLIP-5, 6s)
- 8 generation clips + 1 edit-only segment for 30-second total
- Full clip_segmentation.json with edit_decision_list
- Music rights audit covering all 5 categories
- 4-Part guardrail check completion

### Files

| File | Purpose |
|------|---------|
| `production_brief.md` | Human-readable comprehensive plan |
| `shotlist.csv` | 9 rows including clip_id, trim columns |
| `clip_segmentation.json` | 8 clips + 1 edit-only with assembly order |
| `gpt_image_prompts.jsonl` | 8 image prompts (one per clip first frame) |
| `seedance_prompts.jsonl` | 8 video prompts with multimodal binding |
| `post_production_spec.json` | Complete edit_decision_list + audio + transitions |
| `music_rights_audit.json` | All audio tracks across 5 categories |
| `README.md` | Project-specific context |

### What this demonstrates

**Multi-clip assembly for 30s**:
The video is 30 seconds total but Seedance 2.0 cannot generate more than 15 seconds in one shot. The system handles this automatically with `clip-segmentation` (Pattern A + D combination):

- 8 generation calls (4s/4s/4s/4s/6s/5s/4s/5s = 36s total raw)
- Trimmed and assembled to 27s of visual content
- 3s edit-only segment for subtitle/logo/AI disclosure

**ECU short shots (1.33s each)**:
Seedance has a 4-second minimum. To get 1.33s ECU shots (CLIP-2/3/4), the system generates 4s clips with seed 42 locked for consistency, then specifies `trim_in_frames: 0, trim_out_frames: 64` in the EDL.

**Mirror structure**:
CLIP-1 (dawn clubhouse) and CLIP-8 (dusk clubhouse) share the same composition with different times of day. This creates emotional bookending in 30 seconds.

### Privacy note

Brand names and identifying details have been preserved in this example for educational clarity. If you fork this repository for commercial work, replace `FMGmember` and related strings with your own brand.

## Adding your own example

We welcome examples of:
- Different durations (15s, 60s, 3min)
- Different formats (music video, ad spot, social cut, brand film)
- Different platforms (Reels, Shorts, LinkedIn, Vimeo)
- Failure cases with annotated learnings

To contribute:
1. Mask all personally identifying info (brand names, individuals)
2. Include a README.md explaining context and learnings
3. Submit PR with `examples/<short-descriptive-name>/`

See [CONTRIBUTING.md](../CONTRIBUTING.md).
