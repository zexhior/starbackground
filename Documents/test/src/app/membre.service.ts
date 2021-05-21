import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Numero } from './numero';

@Injectable({
  providedIn: 'root'
})

export class MembreService {
  private baseUrl = "http://127.0.0.1:8000/api";

  constructor(private http: HttpClient) { }

  getMembreList() : Observable<any>{
    return this.http.get(`${this.baseUrl}/membres/`);    
  }

  getMembreById(id: number): Observable<any>{
    return this.http.get(`${this.baseUrl}/membres/${id}`);
  }

  getNumeroById(id: number): Observable<any>{
    return this.http.get(`${this.baseUrl}/numeros/${id}`);
  }

  getNumerosList(): Observable<any>{ 
    return this.http.get(`${this.baseUrl}/numeros/`);
  }

  getMailById(id: number): Observable<any>{
    return this.http.get(`${this.baseUrl}/mails/${id}`);
  }

  getMailList(): Observable<any>{ 
    return this.http.get(`${this.baseUrl}/mails/`);
  }

  getFbById(id: number): Observable<any>{
    return this.http.get(`${this.baseUrl}/fbs/${id}`);
  }

  getFbList(): Observable<any>{ 
    return this.http.get(`${this.baseUrl}/fbs/`);
  }

}
