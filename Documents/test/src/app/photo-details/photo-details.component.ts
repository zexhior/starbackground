import { Component, Input, OnInit } from '@angular/core';
import { ActiviteService } from '../activite.service';
import { Photo } from '../photo';

@Component({
  selector: 'photo-details',
  templateUrl: './photo-details.component.html',
  styleUrls: ['./photo-details.component.scss']
})
export class PhotoDetailsComponent implements OnInit {

  @Input() id:number;
  photo: Photo;
  urlImage: string = "http://127.0.0.1:8000"

  constructor(private activiteService: ActiviteService) { }

  ngOnInit(): void {
    this.reloadData();
  }


  reloadData(){
    this.activiteService.getPhotoById(this.id).subscribe(
      data => {
        this.photo = data;
        this.urlImage += this.photo.url_image;
      }
    )
  }
}
