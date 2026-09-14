# 이미지 에셋 생성 가이드

현재 `assets/img/` 안의 8개 파일은 **플레이스홀더**입니다.
아래 프롬프트로 실사급 이미지를 생성한 뒤, **같은 파일명·같은 비율로 덮어쓰기만 하면** `index.html`은 손댈 필요가 없습니다.

## 공통 규칙

| 항목 | 값 |
|---|---|
| 톤 | cold clinical documentary, cinematic sci-fi, desaturated |
| 색 | slate blue-grey, white, near-black. 따뜻한 색 금지(2막 ECG 제외) |
| 광원 | 단일 저온 광원 + 약한 볼류메트릭. 색온도 6500–8000K |
| 렌즈 | 35mm / 50mm 시네마 렌즈 룩, 얕은 심도, 미세한 필름 그레인 |
| 금지 | 로고·브랜드·판독 가능한 텍스트, 실존 인물 얼굴, 만화체, 네온, UI 오버레이, 워터마크 |

**공통 negative prompt**
```
cartoon, anime, illustration style, 3d render toy look, neon, purple teal grading,
warm skin tones, lens flare, watermark, logo, text, letters, UI overlay,
oversaturated, cheerful, plastic, low detail, deformed anatomy, extra limbs
```

**얼굴 처리** — 모든 인체 컷은 실존 인물로 오인되지 않도록 얼굴을 **비가시 처리**하세요. 성에 낀 유리, 얕은 심도 아웃포커스, 의료용 드레이프, 후두부 앵글 중 하나를 프롬프트에 명시했습니다. 생성물에 또렷한 얼굴이 나오면 재생성하세요.

---

## 00-cover.jpg · 2400×1350 (16:9)

훅 화면. 제목이 왼쪽에 앉으므로 **화면 왼쪽 40%는 비교적 어둡고 단순하게**.

```
Extreme close-up of a frost-covered stainless steel cryogenic dewar surface,
thick white rime crystals creeping across brushed metal, cold nitrogen vapour
drifting slowly in front of the lens, single hard cold key light from upper right,
deep black falloff on the left third of the frame, shallow depth of field,
anamorphic 35mm cinema lens, fine film grain, desaturated slate blue and white,
clinical documentary photography, no text, no logos --ar 16:9
```

## 01-facility.jpg · 2400×1350 (16:9)

숫자 4개가 화면 중앙에 얹히므로 **중앙부는 비워두고 양옆에 탱크**.

```
Wide interior of a clinical cryopreservation storage hall, two rows of tall
polished stainless steel liquid nitrogen dewars receding into darkness on both
sides, an empty dark corridor down the centre of the frame, two technicians in
white sterile gowns and cold-protection gloves standing small in the distance,
faces not visible, low cold overhead lighting, nitrogen vapour pooling on a
polished concrete floor, symmetrical composition, 35mm cinema lens, desaturated
blue-grey and white, photorealistic documentary photography --ar 16:9
```

## 02-capsule.jpg · 2000×2500 (4:5)

몸 안으로 줌인하는 시작 프레임. **화면 정중앙에 흉부**가 오게. 여기서 ×6.4까지 확대되므로 **중앙부 디테일이 살아 있어야** 합니다.

```
A human body lying inside an open cryopreservation capsule, draped in white
sterile medical cloth from the neck down, face obscured behind a frosted glass
panel and shallow focus, chest area sharply in focus at the exact centre of the
frame, condensation and thin ice forming on the capsule's inner rim, cold blue
rim light along the capsule edge, near-black surroundings, clinical and
restrained, vertical composition, photorealistic, 50mm cinema lens,
desaturated slate blue and white --ar 4:5
```

## 03-vessel.jpg · 2400×1350 (16:9)

고급 메디컬 일러스트. 텍스트가 **왼쪽 하단**에 앉습니다 → 좌하단은 어둡게, 주요 혈관은 우측 상단으로.

```
High-end medical illustration, interior of a human blood vessel, endothelial
wall in cross section, a clear viscous cryoprotectant solution advancing through
the vessel and displacing the last dark red blood cells ahead of it, the
solution rendered as a cold translucent blue-white fluid front, subsurface
scattering, scientific accuracy, the vessel running from lower left into upper
right of the frame, dark vignetted lower-left corner, volumetric cold lighting,
desaturated slate blue palette, Scientific American / Nature cover illustration
quality, photoreal microscopy aesthetic --ar 16:9
```

## 04a-ice.jpg · 2000×2000 (1:1)

유리화 컷과 **완전히 같은 구도**여야 비교 슬라이더가 성립합니다. 04b를 먼저 만들고 04a를 variation으로 뽑는 편이 안전합니다.

```
Electron microscopy aesthetic, interior of a single human cell, sharp angular
ice crystals growing outward from the centre and piercing the cell membrane,
the membrane visibly torn and ruptured along the crystal edges, organelles
displaced and crushed, jagged white-blue crystalline shards, cold clinical
lighting, centred square composition, extremely high detail, photorealistic
scientific visualization, desaturated blue-white and black --ar 1:1
```

## 04b-vitrified.jpg · 2000×2000 (1:1)

```
Electron microscopy aesthetic, interior of a single human cell in a vitrified
state, the cytoplasm frozen into a smooth amorphous glass-like solid with no
crystal structure at all, the cell membrane completely intact and unbroken,
organelles preserved in place and clearly visible suspended in transparent
glassy medium, soft internal refraction, cold clinical lighting, identical
framing and scale to the ice-damaged version, centred square composition,
photorealistic scientific visualization, desaturated blue-white and black --ar 1:1
```

> **팁** — Midjourney면 04b 생성 후 `Vary (Subtle)`로 04a를 뽑고 프롬프트만 얼음 결정 쪽으로 바꾸면 구도가 거의 일치합니다. nano-banana / Higgsfield 계열이면 04b를 레퍼런스 이미지로 넣고 편집 프롬프트로 얼음을 추가하세요.

## 05-inverted.jpg · 2000×2500 (4:5)

**중요** — 스크롤에 따라 이 이미지가 180도 회전합니다. 따라서 **머리가 위에 있는 정방향**으로 생성하세요. 웹에서 뒤집습니다.

```
Cross-section cutaway diagram of a tall cylindrical liquid nitrogen dewar,
rendered photorealistically, the outer stainless steel shell cut open to reveal
the interior, a single human body in a white protective sleeping-bag-style
enclosure suspended vertically inside, head at the top of the frame and feet at
the bottom, fully submerged in pale blue liquid nitrogen, cold vapour above the
liquid surface, faces not visible, technical but cinematic, vertical
composition, dark background, desaturated slate blue and white,
photorealistic industrial cross-section --ar 4:5
```

## 06-brain.jpg · 2400×1350 (16:9)

```
Sagittal MRI scan of a human brain dissolving into a dense three-dimensional
network of neurons and synaptic connections, the medical scan layer on the left
half of the frame and the microscopic neural architecture on the right,
fine dendritic filaments, cold blue-white luminance on a near-black background,
scientific visualization, extremely high detail, no text, no scan annotations,
no measurement overlays, cinematic medical documentary --ar 16:9
```

---

## 생성 후 체크리스트

1. **파일명·확장자 동일** (`.jpg`). 파일명이 다르면 화면이 비어 보입니다.
2. **비율 동일**. 다르면 `object-fit:cover`가 잘라내면서 의도한 프레이밍이 깨집니다.
3. **긴 변 2400px 이하, 파일당 400KB 이하**로 압축 (`squoosh.app` 또는 `cwebp -q 82`).
   모바일 데이터 부담을 줄이려면 `.webp`로 만들고 `index.html`의 확장자만 일괄 치환해도 됩니다.
4. **얼굴 판독 불가** 확인.
5. 02 / 03 / 05는 **텍스트가 앉는 영역**(좌하단 또는 중앙)에 밝은 디테일이 몰려 있지 않은지 확인.
6. 04a / 04b의 **구도가 일치**하는지 슬라이더에서 직접 확인.

## 캡션 의무

생성 이미지이므로 푸터에 이미 다음 문구를 넣어 뒀습니다. 지우지 마세요.

> 화면에 쓰인 이미지는 취재 내용을 바탕으로 제작한 재현 이미지이며, 특정 기관이나 인물의 실제 사진이 아닙니다.
