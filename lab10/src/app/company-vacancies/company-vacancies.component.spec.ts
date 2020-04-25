import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CompanyVacanciesComponent } from './company-vacancies.component';

describe('CompanyVacanciesComponent', () => {
  let component: CompanyVacanciesComponent;
  let fixture: ComponentFixture<CompanyVacanciesComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CompanyVacanciesComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CompanyVacanciesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
