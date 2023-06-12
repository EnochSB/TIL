# Django Channels
## 사전준비
- django channels 설치
    ```bash
    python -m pip install -U 'channels[daphne]'
    ```
- 등록
    ```python
    INSTALLED_APPS = (
        "daphne",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.sites",
        ...
    )
    ```
- Docker 설치
    - https://www.docker.com/products/docker-desktop/
    - 가상화 사용 확인
    ![가상화](/Django_practice/images/%EA%B0%80%EC%83%81%ED%99%95%EC%9D%B8.png)
    - Hyper-V 사용
        - 윈도우 Home에서는 따로 설치 필요
            - 하드웨어 요구사항 확인(cmd > systeminfo.exe입력)
                - 두번째 수준 주소 변환(SLAT)을 사용하는 64비트 프로세서.
                - VM 모니터 모드 확장(Intel CPU의 VT-x)을 지원하는 CPU.
                - 최소 4GB 메모리.
                - 가상화 기술(인텔: Intel Virtualiztion Techonlogy, VT-d / AMD: SVM Mode)
                - 하드웨어 적용 데이터 실행 방지.(하드웨어 DEP)
            - 배치파일 준비
                - 메모장에 다음 문구 추가
                    ```txt
                    pushd "%~dp0"
                    dir /b %SystemRoot%\servicing\Packages\*Hyper-V*.mum >hyper-v.txt
                    for /f %%i in ('findstr /i . hyper-v.txt 2^>nul') do dism /online /norestart /add-package:"%SystemRoot%\servicing\Packages\%%i"
                    del hyper-v.txt
                    Dism /online /enable-feature /featurename:Microsoft-Hyper-V -All /LimitAccess /ALL
                    pause
                    ```
                - 파일 > 다른 이름으로 저장.
                - 확장자 .bat으로 지정.
            - 배치파일 실행
                - 관리자 권한으로 실행.
                - 재부팅.
        - Hyper-V 기능 활성화
            - windows 기능 켜기/끄기로 이동
            - Hyper-V 관리도구, 플랫폼 체크
            - 재부팅
            
