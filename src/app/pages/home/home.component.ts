import { Component } from '@angular/core';
import { IBlogEntry } from 'src/app/core/models/blog-entry';
import { BlogService } from 'src/app/core/services/blog.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {
  entry : IBlogEntry[] = [];

  constructor( private blogSvc : BlogService ) {    
    this.entry = blogSvc.posts;
  }

  getBlogEntryList(){
    this.entry = [
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
