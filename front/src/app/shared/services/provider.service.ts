import { EventEmitter, Injectable } from '@angular/core';
import {TaskList, Task} from '../models/models';
import {HttpClient, HttpParams} from '@angular/common/http';
import {MainService} from './main.service';
import {post} from "selenium-webdriver/http";
@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService {
  constructor(http: HttpClient) {
    super(http);
  }

  getPostLists(): Promise<PostList[]> {
    return this.get('http://127.0.0.1:8000/api/post_lists',  {});
  }
  getPost(id: number) {
    return this.get(`http://localhost:8000/api/post_lists/${id}/posts/`, {});
  }

  updatePost(Post) {
    return this.put('http://localhost:8000/api/post_lists/' + post.post_list.id + '/posts/' + post.id, {
      title: post.title,
      body: post.body,
      like_count: post.like_count,
      created_at: post.created_at,
      created_by: post.created_by
    });
  }

  createPost(title: string) {
    console.log(post.id);
    return this.post('http://localhost:8000/api/post_lists/' + post.id + '/tasks/', {
      title: title,
      body: body,
      like_count: post.like_count,
      created_at: Date.now(),
      created_by: created_by
    });
  }
  deletePost(Post) {
    console.log(post.post_list.id);
    return this.delet('http://localhost:8000/api/post_lists/' + post.post_list.id + '/posts/' + post.id, {});
  }

  auth(login: string, password: string): Promise<IAuthResponse> {
    return this.post('http://localhost:8000/api/login/', {
      username: login,
      password: password
    });
  }

  logout(): Promise<any> {
    return this.post('http://localhost:8000/api/logout/', {});
  }

}
