import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BlogEntryPreviewComponent } from './blog-entry-preview.component';

describe('BlogEntryPreviewComponent', () => {
  let component: BlogEntryPreviewComponent;
  let fixture: ComponentFixture<BlogEntryPreviewComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [BlogEntryPreviewComponent]
    });
    fixture = TestBed.createComponent(BlogEntryPreviewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
