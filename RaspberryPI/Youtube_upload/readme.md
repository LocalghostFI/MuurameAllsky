
### Allsky camera scripts     

Youtube Upload tutorial:

1. Download "upload_video.py" file to /home/pi/allsky/scripts/ folder.      
2. Run python upload_video.py  to create a refesh token and authorize to upload videos to the Youtube channel  ([Read more Youtube API this](https://developers.google.com/youtube/v3/guides/uploading_a_video))    
3. Open timelapse.sh file with nano editor and paste this in there. (Or download timelapse.sh file this repo but change title and description )
```sh

if [ "$UPLOAD_VIDEO" = true ] ; then
        if [[ "$PROTOCOL" == "S3" ]] ; then
                $AWS_CLI_DIR/aws s3 cp images/$1/allsky-$1.mp4 s3://$S3_BUCKET$MP4DIR --acl $S3_ACL &
        else
                lftp "$PROTOCOL"://"$USER":"$PASSWORD"@"$HOST":"$MP4DIR" -e "set net:max-retries 1; put images/$1/allsky-$1.mp4; bye" & 
           python3 /home/pi/allsky/scripts/upload_video.py --file=/home/pi/allsky/images/$1/allsky-$1.mp4 --title="Allsky Last Night - $1" --category="28" --keywords="Allsky, timelapse" --description="Allsky last night timelapse. Allsky: <your camera image website url>" --privacyStatus="public" --noauth_local_webserver  &
        fi
fi
```    
