import { Component, OnInit } from '@angular/core';
import {Vacancy} from '../models';
import {ActivatedRoute} from '@angular/router';
import {CompaniesService} from '../companies.service';



@Component({
  selector: 'app-company-vacancies',
  templateUrl: './company-vacancies.component.html',
  styleUrls: ['./company-vacancies.component.css']
})
export class CompanyVacanciesComponent implements OnInit {
  vacancies: Vacancy[];
  constructor(private route: ActivatedRoute, private companiesService: CompaniesService) { }


  ngOnInit(): void {
    this.getVacanciesByCompanyId();
  }


  getVacanciesByCompanyId() {
    const id = +this.route.snapshot.paramMap.get('id');
    this.companiesService.getVacanciesByCompanyId(id).subscribe(vacancies => this.vacancies = vacancies);
  }
}
