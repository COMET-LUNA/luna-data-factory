const {initializeApp} = require('firebase/app')
const {getFirestore, collection, getDoc, addDoc} = require('firebase/firestore')

// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyCMittekZsL95o57e6kyERNtnd7pwZL8fk",
  authDomain: "luna-doctor-finder.firebaseapp.com",
  projectId: "luna-doctor-finder",
  storageBucket: "luna-doctor-finder.appspot.com",
  messagingSenderId: "642725602228",
  appId: "1:642725602228:web:a7847cb3670f4e700248e1",
  measurementId: "G-ZXDTFTXV85"
};

// Initialize Firebase
initializeApp(firebaseConfig)
const firestore = getFirestore();

const findmehistory = require('../json/findmehistory.json')

const findMeHistoryDb = collection(firestore, 'findmehistory')

findmehistory.forEach(item => {
  addDoc(findMeHistoryDb, {
    ...item
  })
})