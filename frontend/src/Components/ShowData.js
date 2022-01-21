import React from "react";
import useFetch from "../Hooks/useFetch";

export const ShowData = ({url = '', method = 'GET', body = null}) => {
    const { isLoading, serverError, apiData } = useFetch(
        method,
        url,
        body
    );

    return (
        <div>
            <h3>API data</h3>
            {isLoading ? <span>Loading.....</span>
              : (!isLoading && serverError) ? (
                <span>Error in fetching data ...</span>
            ) : (
                <span>{`${method} request data: ${JSON.stringify(apiData)}`}</span>
            )}
        </div>
    );
} 