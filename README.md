# Simple RAG Chatbot
이 프로젝트는 Retrieval-Augmented Generation (RAG) 기반의 챗봇을 구현합니다. Gradio를 사용하여 사용자 인터페이스를 제공하며, 다양한 문서 형식(PDF, TXT, Excel, Markdown)을 처리할 수 있습니다.

## 주요 기능
1. **다중 문서 형식 지원**: PDF, TXT, Excel (.xlsx, .xls), Markdown (.md, .markdown) 파일 처리
2. **대화형 인터페이스**: Gradio를 사용한 사용자 친화적 웹 인터페이스
3. **실시간 파일 업로드**: 드래그 앤 드롭으로 새 문서 추가 가능
4. **동적 모델 선택**: 여러 LLM 모델 중 선택 가능
5. **RAG 기반 응답 생성**: 업로드된 문서를 바탕으로 컨텍스트 기반 응답 제공

## 파일 구조
```
simple_rag/
│
├── config/
│   ├── __init__.py
│   └── default_config.yaml
│
├── src/
│   ├── document_processor/
│   │   └── document_processor.py
│   ├── llm/
│   │   └── model.py
│   ├── ui/
│   │   └── gradio_interface.py
│   ├── utils/
│   │   └── file_utils.py
│   └── vector_db/
│       └── chroma_db.py
│
├── data/
│   └── (uploaded documents will be stored here)
│
├── asset/
│   ├── images/
│   │   ├── user.png
│   │   └── chatbot.png
│
├── main.py
├── requirements.txt
├── pyproject.toml
└── README.md
```

## 설치 방법

1. 저장소를 클론합니다:
   ```
   git clone https://github.com/yunwoong7/simple-rag.git
   cd simple-rag
   ```

2. 가상 환경을 생성하고 활성화합니다:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. 필요한 패키지를 설치합니다:
   ```
   pip install -r requirements.txt
   ```

4. `libmagic` 설치 (운영 체제에 따라 다름):
   - macOS: `brew install libmagic`
   - Ubuntu/Debian: `sudo apt-get install libmagic1`
   - CentOS/RHEL: `sudo yum install file-devel`

5. 환경 변수 설정:
   - `OPENAI_API_KEY`와 `GROQ_API_KEY`를 설정합니다.

## 사용 방법

1. 애플리케이션을 실행합니다:
   ```
   python main.py
   ```

2. 웹 브라우저에서 표시된 로컬 URL에 접속합니다.

3. 인터페이스 사용:
   - 문서를 드래그 앤 드롭하여 업로드합니다.
   - LLM 모델을 선택합니다.
   - 질문을 입력하고 엔터를 눌러 챗봇과 대화합니다.
   - "Current Files" 탭에서 업로드된 파일 목록을 확인합니다.
   - "Upload Status" 탭에서 파일 업로드 상태를 확인합니다.

## 주의사항
- 대용량 파일 처리 시 시간이 걸릴 수 있습니다.
- API 키는 안전하게 관리해야 합니다.
