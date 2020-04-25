import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';
import {Company, LoginResponse, Vacancy} from './models';

@Injectable({
  providedIn: 'root'
})
export class CompaniesService {
  constructor(private http: HttpClient) {}


  getCompaniesList(): Observable<Company[]> {
    return this.http.get<Company[]>(`http://localhost:8000/api/companies/`);
  }


  getVacanciesByCompanyId(id: number): Observable<Vacancy[]> {
    return this.http.get<Vacancy[]>(`http://127.0.0.1:8000/api/companies/${id}/vacancies`);
    
  }


  login(username, password): Observable<LoginResponse> {
    return this.http.post<LoginResponse>(`http://127.0.0.1:8000/api/login/`, {
      username,
      password
    });

  }
}
