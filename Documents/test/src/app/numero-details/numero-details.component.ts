import { Component, Input, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { MembreService } from '../membre.service';
import { Numero } from '../numero';

@Component({
  selector: 'numero-details',
  templateUrl: './numero-details.component.html',
  styleUrls: ['./numero-details.component.scss']
})

export class NumeroDetailsComponent implements OnInit {
  
  @Input() id: number;

  telephone: Numero;

  constructor(private membreService: MembreService) { }

  ngOnInit(): void {
    this.reloadData();
  }

  reloadData(){
    this.membreService.getNumeroById(this.id).subscribe(
      data => {
        this.telephone = data;
      }
    );
  }

}
