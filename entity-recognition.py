from google.cloud import language_v1
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/vadithya864/nlp-entity/after-ace-aff54b67811b.json"
def entities_function(text_content):

    client = language_v1.LanguageServiceClient()
    document = {"content": text_content, "type_": language_v1.Document.Type.PLAIN_TEXT, "language": "en"}
    response = client.analyze_entities(request = {'document': document, 'encoding_type': language_v1.EncodingType.UTF8})

    for entity in response.entities:
        print(u"Entity : {}".format(entity.name))

        print(u"Entity type: {}".format(language_v1.Entity.Type(entity.type_).name))

        print(u"Salience score: {}".format(entity.salience))

def main():

    file1 = open("/home/vadithya864/nlp-entity/doc.txt","r")
    text_data = file1.read()
    print(type(text_data),text_data)
    print()
    entities_function(text_data)
    
if __name__ == "__main__":
    main()

    
