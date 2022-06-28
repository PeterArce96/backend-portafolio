import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class FirebaseAdmin:

    def __init__(self):
        cred = credentials.Certificate("app/token.json")
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    def getCollection(self,collectionName):
        lstCollection = []
        collectionValues = self.db.collection(collectionName)
        docValues = collectionValues.get()
        for doc in docValues:
            dicCollection = doc.to_dict()
            #print(doc.id)
            dicCollection.update({'id':doc.id})
            lstCollection.append(dicCollection)
            #print(dicCollection)
        
        return lstCollection

    def getDocument(self,collectionName,documentId):
        docValue = self.db.collection(collectionName).document(documentId).get()
        return docValue.to_dict()

    def updateDocument(self,collectionName,documentId,data):
        docValue = self.db.collection(collectionName).document(documentId).set(data)
        return docValue

    def insertDocument(self,collectionName,data):
        docValue = self.db.collection(collectionName).document().set(data)
        return docValue

    def deleteDocument(self,collectionName,documentId):
        self.db.collection(collectionName).document(documentId).delete()
        return True