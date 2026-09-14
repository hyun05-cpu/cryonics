# 250년 뒤에 깨워주세요 — 냉동인간 인터랙티브

아시아경제 비주얼뉴스. 스크롤 기반 인터랙티브 다큐멘터리.

## 구조

```
.
├── index.html                  ← 전체 코드. CSS/JS 인라인, 의존성 없음
├── assets/
│   ├── img/                    ← 에셋 8종 (현재 플레이스홀더)
│   │   ├── 00-cover.jpg        2400×1350
│   │   ├── 01-facility.jpg     2400×1350
│   │   ├── 02-capsule.jpg      2000×2500
│   │   ├── 03-vessel.jpg       2400×1350
│   │   ├── 04a-ice.jpg         2000×2000
│   │   ├── 04b-vitrified.jpg   2000×2000
│   │   ├── 05-inverted.jpg     2000×2500
│   │   └── 06-brain.jpg        2400×1350
│   └── docs/
│       ├── PROMPTS.md          ← 실사 이미지 생성 프롬프트
│       └── FACTCHECK.md        ← 수치 검증 메모
└── tools/make_placeholders.py  ← 플레이스홀더 재생성용. 배포엔 불필요
```

폰트는 CDN(Pretendard, Noto Serif KR)에서 불러옵니다. 사내망에서 CDN이 막히면 두 `<link>`를 지우면 시스템 폰트로 떨어집니다. 레이아웃은 깨지지 않습니다.

## 배포

```bash
git init
git add .
git commit -m "cryonics interactive"
git branch -M main
git remote add origin https://github.com/<계정>/<저장소>.git
git push -u origin main
```

GitHub → Settings → Pages → Source를 `main` / `root`로 지정.
1–2분 뒤 `https://<계정>.github.io/<저장소>/`에서 열립니다.

## CMS 임베드

기사 본문에는 iframe만 넣습니다. 스크롤 연출물이므로 **화면 전체 높이**를 주고 내부에서 스크롤하게 두는 방식이 안정적입니다.

```html
<iframe
  src="https://<계정>.github.io/<저장소>/"
  title="250년 뒤에 깨워주세요 — 냉동인간 인터랙티브"
  loading="lazy"
  style="display:block;width:100%;height:100vh;border:0;background:#04070A"
  allowfullscreen></iframe>
```

CMS가 인라인 스타일을 막으면:

```html
<iframe src="..." width="100%" height="720" frameborder="0" scrolling="yes"></iframe>
```

### 부모 페이지에서 받는 메시지 (선택)

```js
window.addEventListener("message", function(e){
  if(!e.data || typeof e.data !== "object") return;
  if(e.data.type === "cryo:height"){ /* 문서 전체 높이 */ }
  if(e.data.type === "cryo:vote"){   /* "yes" | "no" — 집계용, 기본은 미저장 */ }
});
```

투표는 **저장하지 않습니다.** 화면에도 그렇게 고지돼 있습니다. 집계하려면 `cryo:vote`를 부모에서 받아 사내 API로 보내고, 고지 문구(`disc`)를 그에 맞게 바꾸세요.

## 이미지 교체

`assets/img/`의 파일을 **같은 이름·같은 비율**로 덮어쓰면 끝입니다. 코드 수정 불필요.
생성 프롬프트는 `assets/docs/PROMPTS.md`.

WebP로 바꾸려면 8개 파일을 변환한 뒤 `index.html`에서 `.jpg` → `.webp` 일괄 치환.

## 연출 구조

| 막 | 화면 | 장치 |
|---|---|---|
| 00 | 훅 — 성에 낀 듀어 | 로드 시 1회 타이틀 시퀀스, 켄번스, 암전 전환 |
| 01 | 숫자 4개 | 스크롤 연동 카운트업 (2억 / 4,000 / 800 / 3) |
| 02 | 법적 사망 | ECG 캔버스. 체온색이 여기서 마지막으로 등장하고 팔레트에서 사라짐 |
| 03 | 혈액 제거 · 냉동보호제 | 8시간 게이지 (00:00 → 08:00) |
| 04 | 몸 안으로 | 캡슐 ×6.4 확대 → 세포 크로스디졸브, 배율 계기 ×1 → ×20,000 |
| 05 | 얼음 vs 유리화 | 드래그 비교 슬라이더 (사용자 조작) |
| 06 | 머리를 아래로 | 이미지 180° 회전 |
| 07 | −196℃ | 36.5 → −196 온도 카운터, 서리 레이어 |
| 08 | 250년 | 2026 → 2276 연도 카운터, 워프 캔버스, 이정표 점등 |
| 09 | 진짜 문제 | 문장 2개, 두 번째만 한랭색 |
| 10 | 뇌 미세구조 | 복구 사례 없음 |
| 11 | 질문 | 2지 선택, 미집계 |

### 텍스트 겹침 방지

모든 문구는 `.beat` 블록이고 `data-band="시작,끝"`으로 **서로 겹치지 않는 스크롤 구간**을 갖습니다. 구간 경계에서만 4.5% 폭으로 교차 페이드하므로, 두 문장이 동시에 읽히는 순간이 없습니다.
문구를 추가·수정할 때는 `data-band` 값이 같은 막 안의 다른 `.beat`와 겹치지 않는지만 확인하면 됩니다.

### 접근성

- `prefers-reduced-motion: reduce`면 스크롤 연출이 꺼지고 **이미지 + 본문이 순서대로 쌓인 읽기 문서**로 전환됩니다.
- 비교 슬라이더는 키보드 좌우 방향키로 조작됩니다.
- JS가 실패해도 모든 문구가 노출됩니다.

## 로컬 확인

```bash
python3 -m http.server 8080
# http://localhost:8080
```
