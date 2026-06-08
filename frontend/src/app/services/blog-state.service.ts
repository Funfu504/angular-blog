import { Injectable } from '@angular/core';
import { BlogService } from 'src/app/services/blog.service';
import { Observable, of, map, switchMap, shareReplay, startWith, Subject } from 'rxjs';
import { IBlogEntry } from '../models/blog-entry';


@Injectable({
  providedIn: 'root'
})
export class BlogStateService {

  constructor(private blogService: BlogService) { }

  private refreshTrigger$ = new Subject<void>();

  posts$ = this.refreshTrigger$.pipe(
    startWith(void 0),
    switchMap(() => this.blogService.getPosts(10)),
    shareReplay(1)
  );

  refreshPosts(): void {
    this.refreshTrigger$.next();
  }
}
