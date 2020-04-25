import { NgModule } from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import { CompaniesComponent } from './companies/companies.component';
import { CompanyVacanciesComponent } from './company-vacancies/company-vacancies.component';

const routes: Routes = [
  { path: 'companies', component: CompaniesComponent },
  { path: 'companies/:id/vacancies', component: CompanyVacanciesComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
