import { Component } from '@angular/core';
import { IBlogEntry, ICreateBlogEntry } from 'src/app/models/blog-entry'
import { FormBuilder, Validators, FormGroup, FormControl } from '@angular/forms';
import { BlogService } from 'src/app/services/blog.service';
import { Observable } from 'rxjs';
import { formatDate } from '@angular/common';
import { Router } from '@angular/router';

@Component({
  selector: 'app-blog-entry-create',
  templateUrl: './blog-entry-create.component.html',
  styleUrls: ['./blog-entry-create.component.css'],
})
export class BlogEntryCreateComponent {

  blogEntry: ICreateBlogEntry | undefined;
  formData: FormData | undefined;
  entry$! : Observable<IBlogEntry | undefined>;
  imagePreview?: string;

  constructor(private fb: FormBuilder, private blogSvc : BlogService, private router: Router) {

  }

 theForm!: FormGroup; 

  ngOnInit() { 
    const today = formatDate(new Date(), 'yyyy-MM-dd', 'en-US');
    
    this.theForm = this.fb.nonNullable.group({    
      image: ['', Validators.required],
      title: ['', Validators.required],		
      blogText: ['', Validators.required],
      summary: ['', Validators.required],
      postDate: [today, Validators.required],
      featured: [true, Validators.required]
    });     
  }

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

      // store preview separately
      this.imagePreview = URL.createObjectURL(file);

  }

  mapFormToCreateRequest(): ICreateBlogEntry {

    const v = this.theForm.getRawValue()

    return {
      title: v.title,
      imageFileName: "",
      imageUrl: "",      
      imageAltText: v.image,
      blogText: v.blogText,
      summary: v.summary,
      postDate: v.postDate,
      featured: v.featured,
      authorId: "Moe"
    };
  }

  onSubmit() {
    
    this.blogEntry = this.mapFormToCreateRequest()    
    this.blogSvc.createBlogPost(this.blogEntry, (this.formData as FormData)).subscribe({
    next: () => {
      this.router.navigate(['/home'], { replaceUrl: true });
    }
  })
  }
}
