import { Component, Input, OnInit } from '@angular/core';
import { Activite } from '../activite';
import { ActiviteService } from '../activite.service';

@Component({
  selector: 'activite-details',
  templateUrl: './activite-details.component.html',
  styleUrls: ['./activite-details.component.scss']
})
export class ActiviteDetailsComponent implements OnInit {
  @Input() id:number;
  @Input() activite: Activite = null;
  urlImage: string = "http://127.0.0.1:8000"

  constructor(private activiteService: ActiviteService) { }

  ngOnInit(): void {
    if(this.activite == null){
      this.reloadData();
    }
  }

  reloadData(){
    this.activiteService.getActiviteById(this.id).subscribe(
      data => {
        this.activite = data;
      }
    )
  }
}
