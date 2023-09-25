import React, { useState, useEffect } from "react";

export function TitleUpdater() {
    const [title, setTitle] = useState('');

    useEffect(() => { document.title = title;}, [title]);
    return (
        <div>
            <input type="text"
                value={title}
                onChange={(e) => setTitle(e.target.value)} />
        </div>
    );
}