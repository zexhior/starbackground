import { Component, Input, OnInit } from '@angular/core';
import { ActiviteService } from '../activite.service';
import { Categorie } from '../categorie';

@Component({
  selector: 'categorie-details',
  templateUrl: './categorie-details.component.html',
  styleUrls: ['./categorie-details.component.scss']
})
export class CategorieDetailsComponent implements OnInit {

  @Input() id: number;
  categorie: Categorie

  constructor(private activiteService: ActiviteService) { }

  ngOnInit(): void {
    this.reloadData();
  }

  reloadData(){
    this.activiteService.getCategorieById(this.id).subscribe(
      data => {
        this.categorie = data;
      }
    )
  }

}
