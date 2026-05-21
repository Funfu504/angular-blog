import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BlogEntryCreateComponent } from './blog-entry-create.component';

describe('BlogEntryCreateComponent', () => {
  let component: BlogEntryCreateComponent;
  let fixture: ComponentFixture<BlogEntryCreateComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [BlogEntryCreateComponent]
    });
    fixture = TestBed.createComponent(BlogEntryCreateComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
