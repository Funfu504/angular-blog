import { Component } from '@angular/core';
import { IBlogEntry } from 'src/app/core/models/blog-entry';
import { BlogService } from 'src/app/core/services/blog.service';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-about',
  templateUrl: './about.component.html',
  styleUrls: ['./about.component.css']
})
export class AboutComponent {
  entry$! : Observable<IBlogEntry | undefined>;

  constructor(private blogSvc : BlogService) { }

  ngOnInit() {
    this.entry$ = this.blogSvc.getAboutMePost();
  }  
}
