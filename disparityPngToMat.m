%% PSMNet disparity.png to disparityMap (mat file) including color map
extension = 'png';
imgPath = ''; % original rectified image for the color map
disparityPath = ''; % disparity.png path
matPath = ''; % .mat path
disparityList = dir([disparityPath '\*.' extension]);
disparityNames = {disparityList.name};
[disparityNames,~] = sortNat(disparityNames);
imgList = dir([imgPath '\*.' extension]);
imgNames = {imgList.name};
[imgNames,~] = sortNat(imgNames);
for i = 1 : length(disparityList)
    disparityPng = imread([disparityPath disparityNames{i}]);
    disparityPng = double(disparityPng);
    disparityMap = disparityPng/256;
    img = imread([imgPath imgNames{i}]);
    img = double(img);
    save(strcat(matPath,'\',num2str(i),'.mat'))
end