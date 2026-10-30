# 오늘의 말씀

성경책 3D 모델을 누르면 표지가 펼쳐지고 페이지가 넘어가며 주제별 랜덤 성경구절(개역한글)이 나타나는 인터랙티브 웹페이지입니다.

- 드래그로 360도 회전, 휠/핀치로 확대
- 주제 선택: 위로 · 힘 · 사랑 · 소망
- 구절 복사, 보관함 저장(localStorage)
- Web Audio로 합성한 종이 넘기는 소리

## 파일

| 파일 | 설명 |
| --- | --- |
| `src.html` | 편집용 소스 (모델 자리에 `__MODEL__` 표시) |
| `book.glb` | 성경책 3D 모델 |
| `build.py` | 모델을 HTML에 넣어 `index.html` 생성 |
| `index.html` | 빌드 결과물, 단독 실행 및 배포용 |

## 수정과 빌드

```bash
python build.py
```

`src.html`이나 `book.glb`를 고친 뒤 실행하면 `index.html`이 다시 만들어집니다.

## 배포

정적 파일이라 `index.html` 하나만 Vercel, GitHub Pages 등에 올리면 됩니다. Three.js와 글꼴은 CDN에서 불러오므로 인터넷 연결이 필요합니다.
