

class Survey extends React.Component {
   render() {
      return (<div>Hello</div>);
   }
}



function initSurveyViewer() {
   var mountP = document.getElementById('surveyMountPoint');
   var survey = <Survey></Survey>;
   ReactDOM.render(survey, mountP);
}


