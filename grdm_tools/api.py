"""Tools to interact with the GakuNin RDM API"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/api.ipynb.

# %% auto 0
__all__ = ['GrdmClient']

# %% ../nbs/api.ipynb 3
import os
# from dotenv import load_dotenv
import requests

# %% ../nbs/api.ipynb 4
class GrdmClient:

    def __init__(self, token:str, domain: str = "rdm.nii.ac.jp"):
        """
        クライアントの初期化

        Args:
            token (str): アクセストークン
            domain (str): ドメイン名
        """
        # load_dotenv()
        # self.token = os.getenv("GRDM_TOKEN")

        self.token = token # api_key

        self.headers = {
            "Authorization": f"Bearer {self.token}"  # 必要に応じてアクセストークンを設定
        }

        self.domain = domain

    def get_users_me(self):
        """
        ユーザ情報を取得する
        """

        url = f"https://api.{self.domain}/v2/users/me/"

        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:

            data = response.json()

            return data
        
        else:

            print("ユーザ情報の取得に失敗しました。ステータスコード:", response.status_code)
            print("レスポンス:", response.text)

            return None

    def upload_file(self, file_path: str, url: str):
        """
        ファイルをアップロードする

        Args:
            file_path (str): ファイルのパス
            url (str): アップロード先のURL
        """
        
        file_name = os.path.basename(file_path)

        upload_url = f"{url}&name={file_name}"

        # Open the file in binary mode and upload it with a PUT request
        with open(file_path, "rb") as f:
            response = requests.put(upload_url, headers=self.headers, data=f)

        # Check the upload result
        if response.status_code == 201:
            print("ファイルが正常にアップロードされました。")
        elif response.status_code == 409:
            print("同じ名前のファイルが既にフォルダに存在します。")
        else:
            print("アップロードに失敗しました。ステータスコード:", response.status_code)
            print("レスポンス:", response.text)

    def update_file(self, file_path: str, url: str):
        """
        ファイルを更新する

        Args:
            file_path (str): ファイルのパス
            url (str): アップロード先のURL
        """
        
        # file_name = os.path.basename(file_path)

        # Add Content-Disposition header with the filename
        headers = self.headers.copy()

        upload_url = f"{url}"

        # Open the file in binary mode and upload it with a PUT request
        with open(file_path, "rb") as f:
            response = requests.put(upload_url, headers=headers, data=f)

        # Check the upload result
        if response.status_code == 200:
            print("ファイルが正常に更新されました。")
        else:
            print("アップロードに失敗しました。ステータスコード:", response.status_code)
            print("レスポンス:", response.text)

    def get_zotero_folder_id(self, project_id):

        url = f"https://api.rdm.nii.ac.jp/v2/nodes/{project_id}/addons/zotero/"
        
        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:

            data = response.json()

            return data["data"]["attributes"]["folder_id"]
        
        else:

            print("フォルダIDの取得に失敗しました。ステータスコード:", response.status_code)
            print("レスポンス:", response.text)

            return None
        
    def get_zotero_contents(self, project_id, folder_id):
        """
        Zoteroのコンテンツを取得する

        Args:
            project_id (str): プロジェクトID
            folder_id (str): フォルダID
        """

        url = f"https://{self.domain}/api/v1/project/{project_id}/zotero/citations/{folder_id}/"

        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:

            data = response.json()

            return data["contents"]
        
        else:

            print("Zoteroのコンテンツの取得に失敗しました。ステータスコード:", response.status_code)
            print("レスポンス:", response.text)

            return None
