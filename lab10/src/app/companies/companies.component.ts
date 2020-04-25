import { Component, OnInit } from '@angular/core';
import { Company } from '../models';
import { CompaniesService } from '../companies.service';

@Component({
  selector: 'app-companies',
  templateUrl: './companies.component.html',
  styleUrls: ['./companies.component.css']
})
export class CompaniesComponent implements OnInit {
  public companies: Company[] = [];
  constructor(private companiesService: CompaniesService) { }


  ngOnInit(): void {
    this.getCompanies();
    console.log(this.companies);
  }


  public getCompanies() {
    this.companiesService.getCompaniesList().subscribe(companies => this.companies = companies);
  }
}
