import { Component } from '@angular/core';
import { IBlogEntry, ICreateBlogEntry } from 'src/app/models/blog-entry'
import { FormBuilder, Validators, FormGroup, FormControl } from '@angular/forms';
import { BlogService } from 'src/app/services/blog.service';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-blog-entry-create',
  templateUrl: './blog-entry-create.component.html',
  styleUrls: ['./blog-entry-create.component.css'],
})
export class BlogEntryCreateComponent {

  blogEntry: ICreateBlogEntry | undefined;
  formData: FormData | undefined;
  entry$! : Observable<IBlogEntry | undefined>;

  constructor(private fb: FormBuilder, private blogSvc : BlogService) {

  }

  theForm = this.fb.nonNullable.group({    
    image: ['', Validators.required],
    title: ['', Validators.required],		
    blogText: ['', Validators.required],
    summary: ['', Validators.required]    
    });  

  ngOnInit() { }

  onFileSelected(event: any) {
    debugger;
    const file: File = event.target.files[0];
    
    if (file) {
      //this.fileName = file.name;
      this.theForm.patchValue({image: file.name})
      this.formData = new FormData();
      this.formData.append("fileName", file.name);
      this.formData.append("contentType", file.type);
      this.formData.append("thumbnail", file);
      this.theForm.get('image')?.updateValueAndValidity();
    }
  }

  mapFormToCreateRequest(): ICreateBlogEntry {

    const v = this.theForm.getRawValue()

    return {
      title: v.title,
      imageUrl: "",
      imageAltText: v.image,
      blogText: v.blogText,
      summary: v.summary,
      postDate: "05/20/2026",
      featured: false,
      authorId: "Moe"
    };
  }

  onSubmit() {
    
    this.blogEntry = this.mapFormToCreateRequest()    
    this.blogSvc.createBlogPost(this.blogEntry, (this.formData as FormData)).subscribe()
  }
}
