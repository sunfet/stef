#开启虚拟机
#cd .\venv\scripts 
#.\activate

#langchain 文档加载器 里面的文本和PDG的加载器
from langchain_community.document_loaders import TextLoader, PyPDFLoader, WebBaseLoader,Docx2txtLoader
#文本分块器:将很长的数据切分
from langchain.text_splitter import RecursiveCharacterTextSplitter
#langchian的openai封装
from langchain_openai import ChatOpenAI
#向量化模型
from langchain_openai import OpenAIEmbeddings

from langchain_community.vectorstores import FAISS
import os


# 方式2：使用HuggingFace的嵌入
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
# 方式3：使用OpenAI的嵌入
from langchain_community.embeddings import OpenAIEmbeddings
from sentence_transformers import SentenceTransformer

base_url = 'https://api.deepseek.com' #llm的接口
model_name = 'deepseek-chat'
api_key = 'sk-cd3005227279412580ca37bee0298709'

def build_knowledge_base():
    file_path = 'text.txt'        #需要投喂的文件
    vector_db_path = 'vector_db'  #把数据向量化之后,保存下来,以后不用再向量化
    # 初始化中文向量模型
    model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
    embeddings = HuggingFaceEmbeddings(model_name='paraphrase-multilingual-MiniLM-L12-v2')
    if not os.path.exists(file_path):
        return FileNotFoundError(f'[!]知识文件不存在')
    if os.path.exists(vector_db_path):  # 如果已经保存过向量数据库,则直接加载
        choice = input("是否需要重新构建向量数据库?(y/n)")
        if choice != 'y':
            return FAISS.load_local(vector_db_path, embeddings, allow_dangerous_deserialization=True)
    
    file_extension = os.path.splitext(file_path)[1].lower()  # 把文件拓展名改小写
    if file_extension == '.txt':
        loader = TextLoader(file_path,encoding='utf-8')
    elif file_extension == '.pdf':
        loader = PyPDFLoader(file_path)
    elif file_extension == '.docx':
        loader = Docx2txtLoader(file_path)
        #TUDO 添加其他文件格式支持

    #加载文档
    documents = loader.load()

    #切块
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,            #文本长度
        chunk_overlap=50            #文本块之间重叠字符的长度
        )
    chunk = text_splitter.split_documents(documents)

    #向量化
    db = FAISS.from_documents(chunk, OpenAIEmbeddings())
    # 保存
    db.save_local(vector_db_path)

    return db
    
    

   




def rag_qa(query,db):
    #初始化大模型
    llm = ChatOpenAI(
        model=model_name,
        api_key=api_key,
        base_url=base_url)
    qa_chain = RetrievalQA.from_chain_type(
        llm,
        chain_type="stuff",                               #检索结果拼接
        retriever=db.as_retriever(search_kwargs={"k": 5}), #数字代表相似度
        # return_source_documents=True
        )
    result = qa_chain(query)
    return result

if __name__ == '__main__':
    #1.构建知识库
    db = build_knowledge_base()
    #2.获取用户的问题
    query = input('请输入你的问题：')

    #3.接受LLM的回复
    answer = rag_qa(query,db)
    #4.打印回答
    print(answer)
