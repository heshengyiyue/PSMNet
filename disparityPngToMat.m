%% PSMNet disparity.png to disparityMap (mat file) including color map
extension = 'png';
imgPath = 'C:\Users\Public\Images\rectified_laparoscope\rectified_left'; % original rectified image for the color map
disparityPath = 'C:\Users\CHEN Jiahe\Documents\GitHub\PSMNet\models\pretrained_model_KITTI2015_results'; % disparity.png path
matPath = [disparityPath '\mat']; % .mat path for output
disparityList = dir([disparityPath '\*.' extension]);
disparityNames = {disparityList.name};
[disparityNames,~] = sortNat(disparityNames);
imgList = dir([imgPath '\*.' extension]);
imgNames = {imgList.name};
[imgNames,~] = sortNat(imgNames);
for i = 1 : length(disparityList)
    disparityPng = imread([disparityPath '\' disparityNames{i}]);
    disparityPng = double(disparityPng);
    disparityMap = disparityPng/256;
    img = imread([imgPath '\' imgNames{i}]);
    colorMap = double(img);
    save(strcat(matPath,'\',num2str(i),'.mat'),'colorMap','disparityMap');
end