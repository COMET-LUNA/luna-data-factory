// Import the functions you need from the SDKs you need
// import { initializeApp } from "firebase/app";
// import { getFirestore } from "firebase/firestore";

const {initializeApp} = require('firebase/app')
const { getAuth, createUserWithEmailAndPassword  } = require('firebase/auth')
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
const auth = getAuth();
const firestore = getFirestore();

// Populate Firebase
const users = require('../json/users.json')
const userDb = collection(firestore, 'users')

users.forEach(user => {
  createUserWithEmailAndPassword(auth, user.email, user.password)
  const {password, ...dbData} = user
  addDoc(userDb, {
    ...dbData
  })
})