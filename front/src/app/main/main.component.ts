import { Component, OnInit } from '@angular/core';
import {Post} from '../../models/models';
import {ProviderService} from 'shared/services/provider.service';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.sass']
})
export class MainComponent implements OnInit {

  constructor() { }

  ngOnInit() {
    this.provider.getPostLists().then(res => {
      this.post = res;
  }

    getPostOfPost(Post) {
      this.provider.getPost(post.id).then(res => {this.posts = res; });
    }


    updatePost(Post) {
      this.provider.updatePost(post).then(res => {});
    }

    deletePost(Post) {
      this.provider.deletePost(post).then(res => {
        this.provider.getPost(post.post_list.id).then(r => {
          this.posts = r;
        });
      });
    }
, status: string, postID: number) {
      let post;
      for(let t in this.post) {
        if(t.id === postID) {
          taskList = t;
          break;
        }
      }
      this.provider.createPost(title).then(res => {
        title = '';
      });
}
