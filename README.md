<h2 align="center">
Simple RAG Chatbot
</h2>

<div align="center">
  <img src="https://img.shields.io/badge/python-v3.9.19-blue.svg"/>
  <img src="https://img.shields.io/badge/langchain-v0.2.12-blue.svg"/>
  <img src="https://img.shields.io/badge/openai-v1.40.1-blue.svg"/>
  <img src="https://img.shields.io/badge/chromadb-v0.5.5-blue.svg"/>
  <img src="https://img.shields.io/badge/gradio-v4.41.0-blue.svg"/>
</div>

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

---

## 데모

#### **1. RAG 없이 LLM만 사용한 경우**

LLM은 다음과 같은 일반적인 응답을 제공했습니다. 응답을 살펴보면, 문구의 언어학적 설명에 그쳤으며, 차량 매뉴얼의 맥락을 전혀 반영하지 못했습니다.

<div align="center">
<img src="https://blog.kakaocdn.net/dn/I8MmP/btsI5wOvWHl/IyzdQbtDKjXVlb9TBbW9xK/img.png" width="70%">
</div>

#### **2. RAG를 사용한 경우**

RAG 시스템은 다음과 같은 구체적이고 정확한 응답을 제공했습니다. 이 응답은 PDF의 다음 내용을 정확히 참조했습니다.

<div align="center">
<img src="https://blog.kakaocdn.net/dn/xajAt/btsI3SFxt7o/QsyhJL48WJKq6GfKGoKjNk/img.gif" width="70%">
</div>

특히 흥미로운 점은 "잠시 휴식을 취하십시오"라는 문구가 실제로는 텍스트가 아니라 차량 디스플레이에 노출되는 이미지라는 것입니다.

<div align="center">
<img src="https://blog.kakaocdn.net/dn/bdCEzW/btsI5aFb7P8/mhrZtIBYCAMXHtsZMV3cEK/img.png" width="70%">
</div>

RAG 시스템이 특정 도메인의 정보를 처리하는 데 있어 LLM의 성능을 크게 향상할 수 있음을 보여줍니다. 특히 기술 문서, 매뉴얼 등 특정 맥락이 중요한 정보를 다룰 때 RAG의 활용이 매우 효과적일 수 있습니다.

---

간단한 RAG 프로그램을 개발해 보았습니다. 이 프로그램은 사용자의 질문에 대해 관련 문서를 검색하고, 이를 바탕으로 LLM이 답변을 생성합니다. 실제 운영 환경에서는 보안, 확장성, 성능 최적화 등 추가적인 고려사항이 필요할 수 있습니다. RAG 기술은 AI 시스템의 정확성과 신뢰성을 크게 향상하는 혁신적인 접근 방식으로, 앞으로 더욱 발전할 것으로 기대됩니다.
