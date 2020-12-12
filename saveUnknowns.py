import crypto
import sys
sys.modules['Crypto'] = crypto
import pyrebase

def UploadUnknowns(path_unknowns):
    config = {
        "apiKey": "AIzaSyBEN3vFrRYYup7Wwnjk0OOaUNWqn2N_4dQ",
        "authDomain": "backup-images-d0747.firebaseapp.com",
        "databaseURL": "https://backup-images-d0747.firebaseio.com",
        "projectId": "backup-images-d0747",
        "storageBucket": "backup-images-d0747.appspot.com",
        "messagingSenderId": "395565925169",
        "appId": "1:395565925169:web:db6a73b3f0a14eb21fa610",
        "measurementId": "G-9PDS7F1ZPZ"
    }
    firebase = pyrebase.initialize_app(config)
    storage = firebase.storage()
    
    name_SavedImg = "images/{}".format(path_unknowns)
    name_SavedImg2 = path_unknowns
    
    storage.child(name_SavedImg).put(name_SavedImg2)
    print("Imagen subida")
