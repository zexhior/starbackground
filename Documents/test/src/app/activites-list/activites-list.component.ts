import { Component, Input, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { Activite } from '../activite';
import { ActiviteService } from '../activite.service';

@Component({
  selector: 'activites-list',
  templateUrl: './activites-list.component.html',
  styleUrls: ['./activites-list.component.scss']
})
export class ActivitesListComponent implements OnInit {
  activites: Observable<Activite[]>

  constructor(private activiteService: ActiviteService) { }

  ngOnInit(): void {
    this.reloadData();
  }

  reloadData(){
    this.activites = this.activiteService.getActiviteList();
  }

}
