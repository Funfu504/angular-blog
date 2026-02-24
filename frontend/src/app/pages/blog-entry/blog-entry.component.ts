import { Component, Input } from '@angular/core';
import { IBlogEntry } from 'src/app/core/models/blog-entry';
import { BlogService } from 'src/app/core/services/blog.service';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-blog-entry',
  templateUrl: './blog-entry.component.html',
  styleUrls: ['./blog-entry.component.css']
})
export class BlogEntryComponent {
  @Input() blogEntryId! : number;
  entry$! : Observable<IBlogEntry | undefined>;
  
  constructor( private blogSvc : BlogService ) {  }
  
  ngOnInit() {
    this.entry$ = this.blogSvc.getPostById(this.blogEntryId);    
  } 

  loadBlogEntry() {
    this.blogSvc
  }
}
