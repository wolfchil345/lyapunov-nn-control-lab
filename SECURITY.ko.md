🌐 언어: [English](SECURITY.md) | [日本語](SECURITY.ja.md) | [한국어](SECURITY.ko.md) | [ไทย](SECURITY.th.md)

# 보안 정책

## 지원 version

`main`의 latest version을 지원합니다. Historical release는 reproducibility를 위해 유지하지만 fix를 받지 않습니다.

## 취약점 보고

Exploit detail을 issue에 공개하지 마십시오. 적절한 private GitHub channel로 repository owner에게 연락하고 affected version, reproduction step, impact, 최소한의 safe example을 제공하십시오.

## 범위

- Unsafe dependency 또는 file-handling behavior.
- Credential, token, private-data exposure.
- Unexpected command execution 또는 untrusted-input handling.
- Workflow와 project script의 security problem.

## 별도의 연구 문제

Numerical instability, model limitations, changed experiment result, scientific interpretation 의견 차이는 software vulnerability가 아닙니다. Sensitive information 없이 research 또는 bug issue로 보고하십시오.

## 안전한 사용

Virtual environment 또는 Codespaces를 사용하고 fork 변경을 검토하며 secret을 commit하지 말고 수정 experiment code 실행 전에 test와 quality-gate workflow를 실행하십시오.
