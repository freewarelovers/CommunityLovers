import { gql } from 'apollo-boost';


export const CREATE_EVENT = gql`mutation  addEvent($name:String!,   $eventCreator:ID!,
    $description: String!, $position:String!, $startAt:Date!){
        addEvent(
                        input : {
                        name:$name, eventCreator:$eventCreator, 
                        description:$description, position:$position, startAt:$startAt}
                    ){
                        errors{field, messages},
                        event{name,slug,position}
                    }
}`

export const ALL_EVENTS = gql`query{
    allEvents{
    id,
      name,
      eventCreator{owner{email}, community{name}}
      slug,
      description,
      position,
      startAt
      
    }
  }`