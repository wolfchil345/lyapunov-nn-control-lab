🌐 언어: [English](../en/codespaces.md) | [日本語](../ja/codespaces.md) | [한국어](../ko/codespaces.md) | [ไทย](../th/codespaces.md)

# GitHub Codespaces 설정

개발 컨테이너는 Python 3.11을 사용하고 `requirements.txt`를 설치하며, 권장 확장 기능과 pytest 테스트 탐색을 설정합니다.

## 첫 명령

```bash
python scripts/check_environment.py
python examples/quick_start.py
make checks
```

## 개발 워크플로

작업용 브랜치를 만들고 변경 범위를 명확히 유지합니다. `make quality-gate`를 실행한 뒤 커밋, 푸시, 풀 리퀘스트 순서로 진행합니다. 생성된 그림은 의도한 참조 산출물일 때만 추적합니다.

추적 중인 바이너리 산출물을 체크아웃하기 전에 Git LFS가 필요합니다. Codespaces 환경이 일치하지 않으면 환경이 생성한 파일을 커밋하지 말고 컨테이너를 다시 빌드합니다.
