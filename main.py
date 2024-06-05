class Rewriter:
    # to perform rewrite on text or essence
    def __init__(self, model, version):
        #初始化，使用的version，rewrite使用的model等
        pass
    
    def rewrite_text(self, text):
        #使用LLM来重写文本，为version 1
        pass
    
    def rewrite_essence(self, essence_before):
        #使用LLM或者其他手段来重写essence，为version 2
        pass
    
    def text_to_essence(self, text):
        #将文本转换成essence，version 1和2都会用到
        pass
    
    def essence_score(self, essence_before, essence_after):
        #输入重写前后的essence，输出相似性分数
        pass