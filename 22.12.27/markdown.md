# 마크다운 문법 정리

## 제목(Heading)
- #의 개수로 소제목 구분(#, ##, ###)

## 리스트(List)
- ol: 순서가 있는 리스트(-, *)
- ul: 순서가 없는 리스트(1, 2, 3 ...)
    - tab으로 하위 항목 구성.

## Fenced Code block
- backtick(`) 기호 3개로 코드를 작성 가능 (```)
- \```python으로 파이썬 코드 작성 시작
    ```python
    print('Hello python')
    #주석
- \```html으로 html 코드 작성 시작
    ```html
    <!-- 주석 -->
## Inline Code block
- 특정 단어를 코드블록으로 사용
- backtick 기호 사이에 \`코드블록\` -> `코드블록`

## Link
- \[문자열](url)을 통해 링크 작성
- ex) \[구글](https://google.com) -> [구글](https://google.com)

## 이미지
- \!\[이미지이름](이미지주소)를 통해 이미지 삽입

## 인용문
- \>로 작성
> 인용문

## 테이블
- |로 작성

\| Syntax | Description |

\| ----------- | ----------- |

\| Header | Title |

\| Paragraph | Text |

| Syntax | Description |
| ----------- | ----------- |
| Header | Title |
| Paragraph | Text |

## 텍스트 강조
- 굵게(\*문자*), 기울임(\**문자**), 취소선(\~~문자~~)

## 수평선
- \---로 작성
---