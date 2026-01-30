import { Injectable } from '@angular/core';
import { IBlogEntry } from '../models/blog-entry';

@Injectable({
  providedIn: 'root'
})
export class BlogService {
  posts : IBlogEntry[] = [];

  constructor() { 
    this.getBlogEntryList();
  }

  getBlogEntryList(){
    this.posts = [
      {    
      id: 1,
      title: "My First Blog Post",
      imageUrl: "/assets/images/FeelsTheCat.jpg",
      imageAltText: "Feels The Cat",
      blogText: "Wall of Text"},
      {    
      id: 2,
      title: "Learning Python",
      imageUrl: "/assets/images/PythonLogo.png",
      imageAltText: "Official Python Logo",
      blogText: "Wall of Text"},
      {    
      id: 2,
      title: "Learning Angular",
      imageUrl: "/assets/images/AngularLogo.png",
      imageAltText: "Angular Logo",
      blogText: "Wall of Text"}
    ]
  }
}
