import { Component } from '@angular/core';
import { IBlogEntry } from '../../core/models/blog-entry';
import { BlogService } from '../../core/services/blog.service';

@Component({
  selector: 'app-blog-entry',
  templateUrl: './blog-entry.component.html',
  styleUrls: ['./blog-entry.component.css']
})
export class BlogEntryComponent {
  entry : IBlogEntry = {
    id: 1,
    title: "My First Blog Post",
    imageUrl: "/assets/images/FeelsTheCat.jpg",
    imageAltText: "Feels The Cat",
    blogText: "Wall of Text"
  }
}
