import { Component } from '@angular/core';
import { IBlogEntry } from '../../core/models/blog-entry';

@Component({
  selector: 'app-blog-entry-preview',
  templateUrl: './blog-entry-preview.component.html',
  styleUrls: ['./blog-entry-preview.component.css']
})
export class BlogEntryPreviewComponent {
  entry : IBlogEntry = {
    id: 2,
    title: "Learning Python",
    imageUrl: "/assets/images/PythonLogo.png",
    imageAltText: "Official Python Logo",
    blogText: "Shortened Wall of Text"
  }
}
