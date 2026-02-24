import { Component, Input } from '@angular/core';
import { IBlogEntry } from '../../core/models/blog-entry';
import { BlogService } from 'src/app/core/services/blog.service';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-blog-entry-preview',
  templateUrl: './blog-entry-preview.component.html',
  styleUrls: ['./blog-entry-preview.component.css']
})
export class BlogEntryPreviewComponent {
   @Input() blogEntryId! : number;
    entry$! : Observable<IBlogEntry | undefined>;

  constructor(private blogSvc : BlogService) { }

  ngOnInit() {
    this.entry$ = this.blogSvc.getPostById(this.blogEntryId);    
  } 
}
