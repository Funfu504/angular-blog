import { Component, Input } from '@angular/core';
import { IBlogEntry } from 'src/app/models/blog-entry';
import { BlogService } from 'src/app/service/blog.service';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-blog-entry-preview',
  templateUrl: './blog-entry-preview.component.html',
  styleUrls: ['./blog-entry-preview.component.css']
})
export class BlogEntryPreviewComponent {
   @Input() blogEntryId! : string;
    entry$! : Observable<IBlogEntry | undefined>;

  constructor(private blogSvc : BlogService) { }

  ngOnInit() {
    this.entry$ = this.blogSvc.getPostById(this.blogEntryId);    
  } 
}
