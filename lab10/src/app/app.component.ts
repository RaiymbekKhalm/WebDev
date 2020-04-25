import {Component, OnInit} from '@angular/core';
import {CompaniesService} from './companies.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})


export class AppComponent implements OnInit {
  title = 'lab10';
  constructor(private companiesService: CompaniesService) { }
  logged = false;
  username = '';
  password = '';


  ngOnInit(): void {
    const token = localStorage.getItem('token');
    if (token) {
      this.logged = true;
    }
  }


  login() {
    this.companiesService.login(this.username, this.password).subscribe(res => {
      localStorage.setItem('token', res.token);
      this.logged = true;
      this.username = '';
      this.password = '';
    });
  }


  logout() {
    localStorage.clear();
    this.logged = false;
    window.location.replace(`http://localhost:4200`);
  }
}
