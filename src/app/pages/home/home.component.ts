import { Component } from '@angular/core';
import { IBlogEntry } from 'src/app/core/models/blog-entry';
import { BlogService } from 'src/app/core/services/blog.service';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {
  entry$! : Observable<IBlogEntry | undefined>;
  previews$! : Observable<IBlogEntry[] | undefined>;

  constructor( private blogSvc : BlogService ) {  }
 
  ngOnInit() {
    this.entry$ = this.blogSvc.getLatestPost();
    this.previews$ = this.blogSvc.getFeaturedPosts(2);
  }  
}
